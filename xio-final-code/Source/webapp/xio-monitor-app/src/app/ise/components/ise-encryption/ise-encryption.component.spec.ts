import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseEncryptionComponent } from './ise-encryption.component';

describe('IseEncryptionComponent', () => {
  let component: IseEncryptionComponent;
  let fixture: ComponentFixture<IseEncryptionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseEncryptionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseEncryptionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
