import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseUnlockComponent } from './ise-unlock.component';

describe('IseUnlockComponent', () => {
  let component: IseUnlockComponent;
  let fixture: ComponentFixture<IseUnlockComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseUnlockComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseUnlockComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
