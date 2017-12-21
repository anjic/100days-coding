import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SanGroupComponent } from './san-group.component';

describe('SanGroupComponent', () => {
  let component: SanGroupComponent;
  let fixture: ComponentFixture<SanGroupComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SanGroupComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SanGroupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
